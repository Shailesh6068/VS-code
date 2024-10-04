package com.example.myapplication

class Myclass1{
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            // Call the add function with positional arguments
            println("The sum of numbers is ${add(5, 11)}")
        }

        // Function to add three integers
        fun add(a: Int, b: Int, c: Int): Int
        {
            return a + b + c
        }

        fun add(a :Int , b:Int):Int
        {
            return a+b
        }
    }
}