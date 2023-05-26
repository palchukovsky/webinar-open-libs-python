cmake_minimum_required(VERSION 3.12)

project(CppLibsForCppAndNotOnly CXX)

if (DEFINED ENV{VCPKG_ROOT} AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
set(CMAKE_TOOLCHAIN_FILE
"$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
CACHE STRING "")
endif()

enable_testing()

add_subdirectory(cpp)

set(CMAKE_CXX_CLANG_TIDY clang-tidy -warnings-as-errors=*)
