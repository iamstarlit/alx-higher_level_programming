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
    const char *value;
    Py_ssize_t length;
    Py_UCS4 *unicode;
    Py_ssize_t i;
    PyUnicodeObject *unicodeObject;

    printf("[.] string object info\n");

    if (PyUnicode_Check(p)) {
        unicodeObject = (PyUnicodeObject *) p;
        length = PyUnicode_GET_LENGTH(p);
        printf("  type: %s\n", "unicode object");

        if (PyUnicode_IS_COMPACT_ASCII(unicodeObject)) {
            value = PyUnicode_AsUTF8AndSize(p, &length);
            printf("  length: %ld\n", length);
            printf("  value: %s\n", value);
        } else {
            printf("  length: %ld\n", length);
            printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
        }

    } else if (PyBytes_Check(p)) {
        printf("  type: %s\n", "bytes");

        PyBytesObject *bytesObject = (PyBytesObject *) p;
        length = PyBytes_GET_SIZE(p);
        value = PyBytes_AsString(p);

        printf("  length: %ld\n", length);
        printf("  value: %s\n", value);

    } else {
        printf("  [ERROR] Invalid String Object\n");
    }
}
