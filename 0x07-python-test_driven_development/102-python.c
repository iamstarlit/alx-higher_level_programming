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
	/* Declare Python Objects */
	PyObject *str, *repr;

	/* Unused variable */
	(void)repr;

	printf("[.] string object info\n");

	/* Check if p is a string object */
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	/* Check if the string is compact ASCII or compact Unicode */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

	/* Get the string representantion of the object */
	repr = PyObject_Repr(p);

	/* Get the encoded string using the utf-8 encoding */
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

	/* Print the length and value of the string object */
	printf(" lenght: %ld\n", PyUnicode_GET_SIZE(p));
	printf(" value: %s\n", PyBytes_AsString(str));
}
