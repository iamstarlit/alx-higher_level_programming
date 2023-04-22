#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object
 *
 * @p: Python object
 *
 * This function prints the type (either compact ASCII or compact Unicode),
 * length, and value of a Python string object.
 */
void print_python_string(PyObject *p)
{
    long int str_len;

    fflush(stdout);

    printf("[.] string object info\n");

    /* Check if object is a string */
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    /* Get the length of the string */
    str_len = ((PyASCIIObject *)(p))->length;

    /* Print the length and value of the string */
    printf(" length: %ld\n", str_len);

    /* Get a wide character string representation of the string */
    wchar_t *wide_str = PyUnicode_AsWideCharString(p, &str_len);
    if (wide_str == NULL)
    {
        printf("  [ERROR] Could not convert string to wide character string\n");
        return;
    }
    printf(" value: %ls\n", wide_str);
    PyMem_Free(wide_str);
}
