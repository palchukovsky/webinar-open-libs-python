###############################################################################

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(pyfibonacci
    module.cpp
    fibonacci.hpp
    fibonacci.cpp)

list(APPEND TARGETS pyfibonacci)


###############################################################################


add_library(fibonacci SHARED
    fibonacci.hpp
    fibonacci.cpp)

list(APPEND TARGETS fibonacci)


###############################################################################


add_executable(fibonacci_test
    fibonacci_test.cpp)

list(APPEND TARGETS fibonacci_test)

find_package(GTest CONFIG REQUIRED)

target_link_libraries(fibonacci_test
    fibonacci
    GTest::gtest_main)

include(GoogleTest)

gtest_discover_tests(fibonacci_test)

add_test(fibonacci fibonacci_test)


###############################################################################


foreach(target ${TARGETS})

    target_compile_features(${target} PUBLIC cxx_std_17)
    set_target_properties(${target} PROPERTIES CXX_STANDARD_REQUIRED ON)

    if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang" OR
        CMAKE_CXX_COMPILER_ID STREQUAL "AppleClang" OR
        CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        target_compile_options(${target}
            PRIVATE -g -Wall -Wextra -Werror -pedantic)
    elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
        target_compile_options(${target}
            PRIVATE /W4 /WX)
    endif()

endforeach()

###############################################################################