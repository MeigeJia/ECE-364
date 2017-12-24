import numpy as np
import zlib
import base64
import re
from PIL import Image
from scipy.misc import imsave

class Payload:
    def __init__(self, rawData=None, compressionLevel=-1, json=None):

        # ERROR CHECKING

        if rawData is None and json is None:
            raise ValueError("Either rawData or json need to be provided!")
        elif compressionLevel not in range(-1,10):
            raise ValueError("Compression Level needs to be in between -1 and 9!")

        if json is None:
            if not isinstance(rawData, np.ndarray) or rawData.dtype != "uint8":
                raise TypeError("rawData needs to be of type uint-8 nd.array!")
        elif rawData is None:
            if type(json) is not str:
                raise TypeError("json needs to be of type 'str'!")

        # SETTING MEMBER VARIABLES
        self.compressionLevel = compressionLevel

        if rawData is not None:
            self.rawData = rawData
            self.RDtoJSON()
        elif json is not None:
            self.json = json
            self.JSONtoRD()

        with open("test.json", "w") as fp:
            fp.write(self.json)

    def RDtoJSON(self):

        # FIND IMAGE TYPE
        types = ['text', 'gray', 'color']
        dimensions = np.shape(self.rawData)
        mode = len(dimensions)  # 1 - Text    2 - Grey    3 - Color
        mode_str = types[mode-1]

        # FIND IMAGE SIZE
        dimensions = np.shape(self.rawData)

        # COMPRESS IMAGE ARRAY
        rawData_raster = self.rawData.flatten()
        if self.compressionLevel > -1:
            rawData_compressed = zlib.compress(rawData_raster, self.compressionLevel)
            is_compressed = 'true'
        else:
            rawData_compressed = rawData_raster
            is_compressed = 'false'

        # ENCODE RAWDATA
        content = str(base64.b64encode(rawData_compressed))[2:-1]

        # GENERATE JSON
        json = '{'+'"type":"{}"'.format(mode_str)
        if mode == 2 or mode == 3:
            json += ',"size":"{}'.format(dimensions[0]) + ',{}"'.format(dimensions[1])
        else:
            json += ',"size":null'
        json += ',"isCompressed":{}'.format(is_compressed)
        json += ',"content":"{}"'.format(content) + '}'
        self.json = json

    def JSONtoRD(self):

        # EXTRACT CONTENT
        type_query = '\"type\":\"(?P<type>color|gray|text)\",'
        size_query = '\"size\":(\"(?P<rows>[0-9]+),(?P<cols>[0-9]+)\"|(?P<null>null)),'
        isCompressed_query = '\"isCompressed\":(?P<isCompressed>true|false),'
        content_query = '\"content\":\"(?P<content>.*)\"'
        totalQuery = '{' + type_query + size_query + isCompressed_query + content_query + '}'
        data = re.match(totalQuery, self.json)
        if data is not None:
            mode_str = data.group("type")
            rows, cols = data.group("rows"), data.group("cols")
            null = data.group("null")
            isString = 0
            if rows is None and cols is None and null is not None:
                isString = 1
            isCompressed = data.group("isCompressed")
            content = data.group("content")
            types = ['text', 'gray', 'color']
            mode = types.index(mode_str)+1

            # DECODE
            content_decoded = base64.b64decode(content)


            # DECOMPRESS
            if isCompressed == 'true':
                content_decompressed = zlib.decompress(content_decoded)
            elif isCompressed == 'false':
                content_decompressed = content_decoded


            # RESHAPE TO NUMPY

            if mode == 1:
                content_decompressed = list(content_decompressed)
                self.rawData = np.array(content_decompressed, dtype=np.uint8)
            elif mode == 2:
                rows = int(rows)
                cols = int(cols)
                content_decompressed = list(content_decompressed)
                content_decompressed = np.array(content_decompressed, dtype=np.uint8)
                content_decompressed = np.reshape(content_decompressed, (rows, cols))
                self.rawData = content_decompressed
            elif mode == 3:
                rows = int(rows)
                cols = int(cols)
                content_decompressed = list(content_decompressed)
                content_decompressed = np.array(content_decompressed, dtype=np.uint8)
                content_decompressed = np.reshape(content_decompressed, (rows, cols, 3))
                self.rawData = content_decompressed
        else:
            raise ValueError("Wrong JSON format!")

class Carrier:
    def __init__(self, img):

        # ERROR CHECKING
        if not isinstance(img, np.ndarray) or img.dtype != "uint8":
            raise TypeError("Carrier Image must be of type 'numpy'!")

        dimensions = np.shape(img)
        if len(dimensions) != 3 or dimensions[2] != 4:
            raise ValueError("Carrier Image must be a 3 dimensional, 4 channel (RGB + ALPHA) image!")

        self.img = img
        self.dimensions = dimensions

    def payloadExists(self):

        # Reading first 8 characters. Checking whether they spell out '{"Type":'
        numCharsToRead = 8
        hiddenJson = ['' for i in range(numCharsToRead)]
        [rows, cols, channels] = self.dimensions
        for charNum in range(numCharsToRead):
            i = charNum//cols
            j = charNum%cols
            channelData = self.img[i,j]  # RGBA values
            a = np.array([[channelData[0]], [channelData[1]], [channelData[2]], [channelData[3]]], dtype=np.uint8)
            b = np.unpackbits(a, axis=1)
            b = np.delete(b, [0,1,2,3,4,5], axis=1)
            letter = np.array([b[3],b[2],b[1],b[0]])
            letter = letter.flatten()
            letter = np.packbits(letter)
            letter = chr(letter)
            hiddenJson[charNum] = letter


        hiddenJson = "".join(hiddenJson)
        if(hiddenJson != '{"type":'):
            return False
        return True

    def clean(self):
        # Taking the last two bits of each channel and shuffling the values around
        # And the original image with the NOT of the previous array.
        # First 6 bits will remain same
        mask = 0b00000011
        lastTwoBits = (self.img & mask)
        np.random.shuffle(lastTwoBits)
        return(self.img & ~lastTwoBits)

    def embedPayload(self, payload, override=False):

        #ERROR CHECKING
        if(type(payload) is not Payload):
            raise TypeError("Input 'payload' must be of type 'Payload'!")

        if type(override) is not bool:
            raise TypeError("Input 'override' must be of type 'bool'!")

        maxSize = self.dimensions[0] * self.dimensions[1]
        payloadSize = len(payload.json)

        if(payloadSize > maxSize):
            raise ValueError("Payload too large for Carrier!")

        if override is False and self.payloadExists():
            raise Exception("Carrier already holds a payload. Either turn on override, or switch the current carrier.")

        # EMBEDDING PAYLOAD INTO CARRIER
        # read carrier image dimensions and create copy
        cleaned_carrier = self.img.copy()
        dimensions = np.shape(cleaned_carrier)
        [rows, cols, channels] = dimensions
        cleaned_carrier = cleaned_carrier.reshape(rows*cols, channels)

        # Convert json into a numpy array. Each index contains the asci value of one alphabet.
        json = list(payload.json)
        f = lambda x: ord(x)
        json = list(map(f, json))
        json_array = np.array(json)

        # Find length of json array (n). For the first n elements in the carrier array, set the the 2 least significant
        # bits to 0. These two bits will be used to store the json data.
        jsonLength = len(json)
        mask = 0b11111100
        cleaned_carrier[0:jsonLength,:] = np.bitwise_and(cleaned_carrier[0:jsonLength,:], mask)

        # Create a new numpy array that will hold the data to be embedded. All indices from n to length of the
        # carrier image will hold 0. This is because only the first n elements will have actual data.
        lastTwoBits = cleaned_carrier.copy()
        mask = 0b00000000
        lastTwoBits[jsonLength:, :] = mask

        # Extract data to be held by each channel of each pixel.
        alpha = np.right_shift(json_array, 6)
        alpha = np.bitwise_and(alpha,3)
        blue = np.right_shift(json_array, 4)
        blue = np.bitwise_and(blue,3)
        green = np.right_shift(json_array, 2)
        green = np.bitwise_and(green,3)
        red = np.right_shift(json_array, 0)
        red = np.bitwise_and(red,3)

        # Store channel data in lastTwoBits array. this array is one long array whose length is equal to the number
        # of pixels present. For each index, the array extends backward for 4 indices. These indices contain the data
        # to be embedded into its corresponding channel. This array is then added to the carrier array, whose two least
        # significant bits were set to 0.
        lastTwoBits[:jsonLength, 0] = red
        lastTwoBits[:jsonLength, 1] = green
        lastTwoBits[:jsonLength, 2] = blue
        lastTwoBits[:jsonLength, 3] = alpha
        result = np.add(cleaned_carrier, lastTwoBits)
        result = result.reshape((rows, cols, channels))

        return result

    def extractPayload(self):

        # The last two bits of each channel is extracted. Each pixel represents one character.
        carrier = self.img
        red = carrier[:, : , 0].flatten()
        green = carrier[:, :, 1].flatten()
        blue = carrier[:, :, 2].flatten()
        alpha = carrier[:, :, 3].flatten()

        red = np.reshape(red, (red.shape[0], 1))
        red = np.unpackbits(red, axis=1)
        red = np.delete(red, [0,1,2,3,4,5], axis=1)

        green = np.reshape(green, (green.shape[0], 1))
        green = np.unpackbits(green, axis=1)
        green = np.delete(green, [0,1,2,3,4,5], axis=1)

        blue = np.reshape(blue, (blue.shape[0], 1))
        blue = np.unpackbits(blue, axis=1)
        blue = np.delete(blue, [0,1,2,3,4,5], axis=1)

        alpha = np.reshape(alpha, (alpha.shape[0], 1))
        alpha = np.unpackbits(alpha, axis=1)
        alpha = np.delete(alpha, [0,1,2,3,4,5], axis=1)

        json = np.zeros((red.shape[0], 8), dtype="uint8")
        json[:, 0:2] = alpha
        json[:, 2:4] = blue
        json[:, 4:6] = green
        json[:, 6:8] = red
        json = np.packbits(json, axis=1)
        json = json.flatten()
        json = json.tolist()
        f = lambda x: chr(x)
        json = list(map(f, json))
        json = "".join(json)
        json = json[0:json.find("}")+1]

        payload = Payload(None, -1, json)
        return payload


##### TESTING FUNCTIONS #####

# def pullJson(fname):
#     dir = "projectfiles/data/"
#     file = dir+fname
#     with open(file, "r") as fp:
#         for i,line in enumerate(fp):
#             a = line
#     return a # string
#
# def pullText(fname):
#     dir = "projectfiles/data/"
#     file = dir+fname
#     with open(file, "r") as fp:
#         data = fp.readlines()
#     data = "".join(data)
#     data = list(data)
#     f = lambda x: ord(x)
#     data = list(map(f, data))
#     a = np.array(list(data), dtype="uint8")
#     return a # numpy array
#
# def pullImage(fname):
#     dir = "projectfiles/data/"
#     file = dir+fname
#     im = np.asarray(Image.open(file))
#     return im # numpy array
#
# def pushJson(payload, fname):   # payload must be of class "Payload"
#     json = payload.json
#     # print(json)
#     # f = lambda x: chr(x)
#     # json = list(map(f, json))
#     # json = "".join(json)
#     with open(fname, "w+") as fp:
#         fp.write(json)
#
# def pushText(payload, fname):
#     text = payload.rawData.tolist()
#     f = lambda x: chr(x)
#     text = list(map(f, text))
#     text = "".join(text)
#     with open(fname, "w+") as fp:
#         fp.write(text)
#
# def pushImage(payload, fname):
#     imsave(fname, payload.rawData)
#
# def compareFiles(res, ans):
#     dir = "projectfiles/data/"
#     with open(res) as fp:
#         data1 = fp.readlines()
#     data1 = "".join(data1)
#     # print("My answer:", data1[0:100])
#
#     with open(dir+ans) as fp:
#         data2 = fp.readlines()
#     data2 = "".join(data2)
#     # print("Actual answer:", data2[0:100])
#
#     if(data1 == data2):
#         print("PASSED!")
#     else:
#         print("FAILED :(")
#
# def compareImages(res, ans):
#     res_img = np.asarray(Image.open(res))
#     ans_img = pullImage(ans)
#     if np.array_equal(res_img, ans_img):
#         print("PASSED!")
#     else:
#         print("FAILED :(")
#
# #############################
#
#
# # if __name__ == '__main__':
#     #
#     # # TEST CASE 1
#     # print("Test Case 1 - ")
#     # inp = "payload1.png"
#     # out = "test.json"
#     # ans = "payload1.json"
#     # img = pullImage(inp)
#     # payload = Payload(img, -1, None)
#     # pushJson(payload, out)
#     # compareFiles(out, ans)
#     #
#     # # TEST CASE 2
#     # print("Test Case 2 - ")
#     # inp = "payload2.png"
#     # out = "test.json"
#     # ans = "payload2.json"
#     # img = pullImage(inp)
#     # payload = Payload(img, 7, None)
#     # pushJson(payload, out)
#     # compareFiles(out, ans)
#     #
#     # # TEST CASE 3
#     # # print("Test Case 3 - ")
#     # # inp = "payload3.txt"
#     # # out = "test.json"
#     # # ans = "payload3.json"
#     # # img = pullText(inp)
#     # # payload = Payload(img, 5, None)
#     # # pushJson(payload, out)
#     # # compareFiles(out, ans)
#     #
#     # # TEST CASE 4
#     # print("Test Case 4 - ")
#     # inp = "payload1.json"
#     # out = "test.png"
#     # ans = "payload1.png"
#     # json = pullJson(inp)
#     # payload = Payload(None, -1, json)
#     # pushImage(payload, out)
#     # compareImages(out, ans)
#     #
#     # # TEST CASE 5
#     # print("Test Case 5 - ")
#     # inp = "payload2.json"
#     # out = "test.png"
#     # ans = "payload2.png"
#     # json = pullJson(inp)
#     # payload = Payload(None, -1, json)
#     # pushImage(payload, out)
#     # compareImages(out, ans)
#     #
#     # # TEST CASE 6
#     # print("Test Case 6 - ")
#     # inp = "payload3.json"
#     # out = "test.txt"
#     # ans = "payload3.txt"
#     # json = pullJson(inp)
#     # payload = Payload(None, -1, json)
#     # pushText(payload, out)
#     # compareFiles(out, ans)
#
#     # TEST CASE 7
#     # print("Test Case 7 - ")
#     # inp = "payload2.json"
#     # out = "test.png"
#     # ans = "payload2.png"
#     # json = pullJson(inp)
#     # payload = Payload(None, -1, json)
#     #
#     # inp2 = "carrier.png"
#     # carrier_img = pullImage(inp2)
#     # carrier = Carrier(carrier_img)
#     # carrier_embedded = carrier.embedPayload(payload)
#     #
#     # carrier2 = Carrier(carrier_embedded)
#     # payload2 = carrier2.extractPayload()
#     # pushImage(payload2, out)
#     #
#     # compareImages(out, ans)
#
#  # # LOAD IMAGE
#  #    dir = "projectfiles/data/"
#  #    fname = "carrier.png"
#  #    file = dir+fname
#  #    im = np.asarray(Image.open(file)) # raw data - 3d rgb numpy array
#  #    x = Carrier(im)
#  #    x.payloadExist()
#  #    x.clean()
#  #    x.payloadExist()
#  #
#  #    # LOAD IMAGE
#  #    dir = "projectfiles/data/"
#  #    fname = "payload2.png"
#  #    file = dir+fname
#  #    im = np.asarray(Image.open(file)) # raw data - 3d rgb numpy array
#  #    y = Payload(im, -1, None)
#  #
#  #    x.embedPayload(y, True)
#  #    print(x.payloadExist())
#     #x.extractPayload()
# #################################
#
#     # LOAD JSON
#     # dir = "projectfiles/data/"
#     # jsonFile = 'payload3.json'
#     # file = dir+jsonFile
#     # with open(file, "r") as fp:
#     #     for i,line in enumerate(fp):
#     #         a = line
#     #
#     # x = Payload(None, -1, a)
#     # temp = x.rawData.tolist()
#     # f = lambda x: chr(x)
#     # temp = list(map(f, temp))
#     # temp = "".join(temp)
#     #
#     # with open("test.txt", "w+") as fp:
#     #     fp.write(temp)
#
#
#
#
#     # LOAD TEXT
#     # dir = "projectfiles/data/"
#     # textFile = "payload3.txt"
#     # file = dir+textFile
#     # with open(file, "r") as fp:
#     #     data = fp.readlines()
#     # data = "".join(data)
#     # data = list(data)
#     # f = lambda x: ord(x)
#     # data = list(map(f, data))
#     # a = np.array(list(data), dtype="uint8")
#     # for i in range(4,7):
#     #     print("Compression = ", i)
#     #
#     #     x = Payload(a, i, None)
#     #
#     #     res = "test.json"
#     #     ans = "payload3.json"
#     #
#     #     with open(res) as fp:
#     #         data1 = fp.readlines()
#     #     data1 = "".join(data1)
#     #     print("My answer:", data1[0:100])
#     #
#     #     with open(dir+ans) as fp:
#     #         data2 = fp.readlines()
#     #     data2 = "".join(data2)
#     #     print("Actual answer:", data2[0:100])
#     #
#     #     if(data1 == data2):
#     #         print("COMPRESSION LEVEL IS", i)
#     #     print("")
