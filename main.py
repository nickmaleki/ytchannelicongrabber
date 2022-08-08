# get channel id:
# https://commentpicker.com/youtube-channel-id.php
#
# search by custom channel using:
# https://www.googleapis.com/youtube/v3/search?part=id%2Csnippet&q=UCFeIEAkqvS4fJMTwUtF4OFw&type=channel&fields=items(id%2Csnippet%2Fthumbnails%2Fhigh%2Furl,%2Csnippet%2Ftitle)&key=
#
# Get by channel data (Doesn't work for custom URLs) where id=commaseperatedlistofchannelids
# GET https://www.googleapis.com/youtube/v3/channels?part=snippet&id=UCnxQ8o9RpqxGF2oLHcCn9VQ&fields=items(id%2Csnippet%2Fthumbnails%2Fhigh%2Furl,%2Csnippet%2Ftitle)&key=
#
# convert to base64
# https://base64.guru/converter/encode/image/png

from urllib.request import urlopen
import base64
import json
import cairosvg

# ["Miegakure","marctenbosch"."vihart","aleph0", "whatdamath", "UCsooa4yRKGN_zEE8iknghZA","UCrv269YwJzuZL3dH5PCgxUw", "veritasium", "numberphile", "UCs4aHmggTfFrpkPcWSaBN9g", "UCYO_jab_esuFRV4b17AJtAw"]
channel_search = ["MoltenScience"]
API_KEY = ""

for channel in channel_search:
    contents = json.load(urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=id%2Csnippet&q=" + channel + "&type=channel&fields=items(id%2Csnippet%2Fthumbnails%2Fhigh%2Furl,%2Csnippet%2Ftitle)&key=" + API_KEY))
    channel_title = contents["items"][0]['snippet']['title']
    channel_title_length = len(channel_title)
    thumbnail_url = contents["items"][0]['snippet']["thumbnails"]["high"]["url"]
    # yt_x = 405.46679 + ((516.59248 - 405.46679) / 24 * channel_title_length)
    # rect_x = 417.27917 + ((521.35913 - 417.27917) / 24 * channel_title_length)
    # rect_width = 28.312683 + ((132.39267 - 28.312683) / 24 * channel_title_length)
    # rect_width = 132.39267

    # Code to fill svg template #
    #
    # base64_thumbnail = base64.b64encode(urlopen(thumbnail_url).read()).decode("utf-8")
    # with open("template2160.svg", "rt") as fin:
    #     with open(channel_title + ".svg", "wt") as fout:
    #         for line in fin:
    #             fout.write(line.replace('channel_title', channel_title).replace('base64_thumbnail', base64_thumbnail))
    #             # .replace('yt_x', str(yt_x)).replace('rect_x', str(rect_x)).replace('rect_width', str(rect_width)
    #
    # cairosvg.svg2png(url=channel_title + ".svg", write_to=channel_title + ".png")

    # Code to dump raw png #
    png_recovered = urlopen(thumbnail_url).read()
    f = open(channel_title + ".png", "wb")
    f.write(png_recovered)
    f.close()
