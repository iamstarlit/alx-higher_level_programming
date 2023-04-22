#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 * @p: Python Object
 *
 * Description: This function prints information about a Python string object.
 * It checks whether the object passed is indeed a string, prints its type
 * (either compact ASCII, compact Unicode, or legacy string), its length, and its value.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    char *value;

    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        if (PyUnicode_IS_ASCII(p))
        {
            printf("  type: compact ascii\n");
        }
        else
        {
            printf("  type: compact unicode object\n");
        }
        length = PyUnicode_GET_LENGTH(p);
        value = PyUnicode_AsUTF8AndSize(p, &length);
        printf("  length: %ld\n", length);
        printf("  value: %s\n", value);
    }
    else if (PyBytes_Check(p))
    {
        printf("  type: bytes\n");
        length = PyBytes_GET_SIZE(p);
        value = PyBytes_AsString(p);
        printf("  length: %ld\n", length);
        printf("  value: %s\n", value);
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}
