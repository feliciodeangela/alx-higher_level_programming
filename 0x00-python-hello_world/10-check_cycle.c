#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: List to check.
 * Return: 0 | 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *cur = list, *aux = list;
	int i = 0, j = 0;

	while (cur != NULL)
	{
		while (i >= j)
		{
			if (cur->next == aux || cur->next == cur)
				return (1);
			aux = aux->next;
			j++;
		}
		aux = list;
		cur = cur->next;
		i++;
	}
	return (0);
}
