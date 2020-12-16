#include "lists.h"
/**
 * is_palindrome - finds palindromism in a lits
 * @head: pointer to the first node
 * Return: Returns 1 if palindrome or else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int count = 0, len = 0, iter = 0;
	int buffer[9999];

	if (!head || !*head || !temp->next )
		return (1);

	while (temp)
	{
		buffer[count] = temp->n;
		count++;
		temp = temp->next;
	}

	len = count -1;
	while (iter <= len)
	{
		if (buffer[iter] != buffer[len])
			return (0);
		iter++;
		len--;
	}
	return (1);
}
