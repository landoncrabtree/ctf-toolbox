import zlib
import base64

# SYsTem.IO.comPreSsION.DefLAtEstrEaM( [sYSTEm.iO.MemOrYstreAM][COnveRt]::FRomBase64STRing('b64 here' ) ,[io.cOMpreSSIoN.coMPrESsiOnMOde]::deCoMpRESs

b64 = 'base64 goes here'

compressed_data = base64.b64decode(b64)
decompressed_data = zlib.decompress(compressed_data, -15)
print(decompressed_data.decode('utf-8', 'ignore'))
