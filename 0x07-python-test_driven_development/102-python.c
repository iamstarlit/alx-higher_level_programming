#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 * @p: Python Object
 *
 * Description: This function prints information about a Python string object.
 * It checks whether the object passed is indeed a string, prints its type
 * (either compact ASCII or compact Unicode), its lenght, and its value.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Lenght of the string */
	length = ((PyASCIIObject *)(p))->length;

	/* Print the length and value of the string object */
	printf(" lenght: %ld\n", length);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
