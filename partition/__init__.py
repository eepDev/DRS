# from partition.ntfsbootsector import NtfsBootSector
#
# if __name__ == "__main__":
#     from partition.partitionmanager import PartitionManager
#     print("NTFS Partitions:")
#     partitions = PartitionManager.load_partitions()
#     for partition in partitions:
#         print("path:" + partition.path + ", size:" + 'partition.size' + ", label:" + partition.label)
#         print(partition.read_data(0, 512))
#         print('MFT location:')
#         # print(NtfsBootSector(partition.read_data(0, 1)).get_mft_start_offset())
