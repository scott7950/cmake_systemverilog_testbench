PROJECT("CMake_SVTB")
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

#SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules")

ADD_SUBDIRECTORY(rtl)
ADD_SUBDIRECTORY(env)
ADD_SUBDIRECTORY(test)
ADD_SUBDIRECTORY(script)
ADD_SUBDIRECTORY(sim)

