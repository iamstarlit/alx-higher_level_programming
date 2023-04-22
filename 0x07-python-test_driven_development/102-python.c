#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    const char *value;

    printf("[.] string object info\n");

    if (PyUnicode_Check(p))
    {
        if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("  type: compact ascii\n");
        else
            printf("  type: compact unicode object\n");
        value = PyUnicode_AsUTF8AndSize(p, &length);
        printf("  length: %ld\n", length);
        printf("  value: %s\n", value);
    }
    else if (PyBytes_Check(p))
    {
        printf("  type: bytes object\n");
        value = PyBytes_AsString(p);
        length = PyBytes_Size(p);
        printf("  length: %ld\n", length);
        printf("  value: %s\n", value);
    }
    else
    {
        printf("  [ERROR] Invalid String Object\n");
    }
}
