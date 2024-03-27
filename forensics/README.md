# Memory Analysis
* [volatility/volatility.sh](volatility/volatility.sh) - Installation script for volatility2 and volatility3

# Network Forensics
* [NetworkMiner](https://www.netresec.com/index.ashx?page=NetworkMiner) - A tool for analyzing network traffic.
* [dShell]( https://github.com/USArmyResearchLab/Dshell) - A network forensic analysis framework.
* [WireShark](https://www.wireshark.org/) - A tool for analyzing network traffic.
* [http-ripper](https://github.com/landoncrabtree/http-ripper) - Dumps HTTP 206 partial content into a file.
* [wireshark2bytes.py](wireshark2bytes.py) - Converts Wireshark hexdump to bytes. Useful for exporting files from Wireshark streams.

## Raw Packet -> Pcap
[Reference](https://tshark.dev/edit/text2pcap/)
```bash
xxd -g 1 packet.raw > packet_formatted.raw
text2pcap packet_formatted.raw packet.pcap
```
