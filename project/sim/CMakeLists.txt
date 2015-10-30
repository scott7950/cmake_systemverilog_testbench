SET(DO_TCL ${PROJ_SCRIPT_DIR}/do.tcl)

foreach (INC_DIR ${ENV_INC})
    SET(INC_DIR_FLAGS ${INC_DIR_FLAGS} +incdir+${INC_DIR})
endforeach()

SET(FILE_LIST ${VERILOG_SRC_FILES} ${TB_ENV_FILES} ${TOP_ENV_FILES} ${TEST_FILES})

ADD_CUSTOM_COMMAND(
    OUTPUT work/
    COMMAND vlib work
    COMMENT "Generating modelsim work library"
)

ADD_CUSTOM_COMMAND(
    OUTPUT work/_vmake
    COMMAND vlog -novopt -sv -timescale "1ns/1ps" "$(VLOG_EXTRA_ARG)" ${INC_DIR_FLAGS} ${FILE_LIST}
    DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/work
    COMMENT "Compiling Verilog files: ${VERILOG_SRC_FILES}"
)

ADD_CUSTOM_COMMAND(
    OUTPUT transcript
    COMMAND vsim -novopt -c "$(VSIM_EXTRA_ARG)" -do ${DO_TCL} work.${TOP_TB_NAME}
    DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/work/_vmake
    COMMENT "Run simulation"
)

ADD_CUSTOM_TARGET(compile DEPENDS work/_vmake)
ADD_CUSTOM_TARGET(sim DEPENDS transcript)

