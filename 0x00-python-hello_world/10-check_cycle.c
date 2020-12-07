#include "lists.h"
/**
 * check_cycle - check if a singly list has a cycle in it
 * @list: specific list
 * Return: 0 if not cycle 1 if there is a cycle
 **/
int check_cycle(listint_t *list)
{
	int i = 0;

	if (!list)
		return (0);
	while (list)
	{
		list = list->next;
		i++;
		if (i > 100)
			return (1);
	}
	return (0);
}

