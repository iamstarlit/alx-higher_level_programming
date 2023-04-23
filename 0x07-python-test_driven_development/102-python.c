#include <Python.h>
#include <stdio.h>

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
    Py_UNICODE *unicode;
    char *value;
    unsigned int i, kind;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    unicode = PyUnicode_AsUnicode(p);
    kind = PyUnicode_KIND(p);

    if (kind == PyUnicode_1BYTE_KIND) {
        value = (char *) PyUnicode_1BYTE_DATA(p);
        printf("  type: compact ascii\n");
    }
    else if (kind == PyUnicode_2BYTE_KIND) {
        value = (char *) PyUnicode_2BYTE_DATA(p);
        printf("  type: compact unicode object\n");
    }
    else if (kind == PyUnicode_4BYTE_KIND) {
        value = (char *) PyUnicode_4BYTE_DATA(p);
        printf("  type: compact unicode object\n");
    }
    else {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("  length: %ld\n", length);
    printf("  value: ");

    for (i = 0; i < length; i++) {
        if (kind == PyUnicode_1BYTE_KIND)
            putchar(value[i]);
        else
            printf("%04x", unicode[i]);
    }

    putchar('\n');
}
