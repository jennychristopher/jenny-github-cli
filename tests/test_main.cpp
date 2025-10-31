#include <gtest/gtest.h>

// Forward declare the functions from main.cpp
//int add(int a, int b);
//int mul(int a, int b);
#include "../src/muladd.h"

// Test cases
TEST(MathTests, AddTest) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_EQ(add(-1, 1), 0);
    EXPECT_EQ(add(0, 0), 0);
}

TEST(MathTests, MulTest) {
    EXPECT_EQ(mul(2, 3), 6);
    EXPECT_EQ(mul(-2, 3), -6);
    EXPECT_EQ(mul(0, 5), 0);
}

// Standard GTest entry point
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

