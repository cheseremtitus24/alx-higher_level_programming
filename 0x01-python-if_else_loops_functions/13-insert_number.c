#include "lists.h"
/**
 * insert_node- inserts an element at right position in a sorted linked list
 * @head: Pointer to the head of the linked list
 * @number: value to save to list
 *
 * Return: new node else NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *tmp;
	int insert_end;

	current = *head;
	insert_end = 0;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else if (number < (*head)->n)
	{
		new->next = (*head);
		*head = new;
	}
	else
		{
			while (current->next != NULL)
			{
				if ((current->next->n) >= new->n)
				{
					tmp = current->next;
					current->next = new;
					new->next = tmp;
					insert_end++;
					break;
				}
				current = current->next;
			}
			if (insert_end < 1)
				current->next = new;
		}
	return (new);
}

