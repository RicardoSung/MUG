# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/MUG_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/MUG_autogen.dir/ParseCache.txt"
  "MUG_autogen"
  )
endif()
