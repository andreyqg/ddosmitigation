# Comment when NO logging desired
#BMV2_SWITCH_EXE = ~/behavioral-model/targets/simple_switch_grpc/simple_switch_grpc
# Uncomment to execute NO logging
BMV2_SWITCH_EXE = simple_switch_grpc
NO_P4 = true
P4C_ARGS = --p4runtime-files $(basename $@).p4.p4info.txt

include ./utils/Makefile
