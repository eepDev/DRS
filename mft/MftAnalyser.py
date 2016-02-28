import struct

from partition import NtfsPartition, NtfsBootSector


class MftAnalyser:
    SECTOR_SIZE = 512

    def __init__(self, partition: NtfsPartition):
        self.partition = partition

    def analyse(self):
        # TODO:
        # 1. find location of MFT
        mft_offset = NtfsBootSector(self.partition.read_data(0, 1)).get_mft_start_offset()
        pass
