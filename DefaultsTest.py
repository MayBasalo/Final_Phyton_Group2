# Import

import FormatValues as FV

# Reading Defaults.dat File

f = open('./DataFiles/Defaults.dat', 'r')
NexTranNum = int(f.readline())
NexDriNum = int(f.readline())
MonStaFee = float(f.readline())
DaiRenFee = float(f.readline())
WeekRenFee = float(f.readline())
HST = float(f.readline())
f.close()

# Incrementing things

NexTranNum += 1
NexDriNum += 1

# Doing more stuff with Defaults.dat file

f = open("./DataFiles/Defaults.dat", 'w')
f.write(f"{str(NexTranNum)}\n")
f.write(f"{str(NexDriNum)}\n")
f.write(f"{str(FV.FComma2(MonStaFee))}\n")
f.write(f"{str(FV.FComma2(DaiRenFee))}\n")
f.write(f"{str(FV.FComma2(WeekRenFee))}\n")
f.write(f"{str(HST)}\n")
f.close()

# Printing things

print(NexTranNum)
print(NexDriNum)
print(FV.FDollar2(MonStaFee))
print(FV.FDollar2(DaiRenFee))
print(FV.FDollar2(WeekRenFee))
print(HST)