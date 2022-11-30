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

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
		{
			while (current->next != NULL)
			{
				if ((current->next->n) >= new->n || current->next == NULL)
				{
					tmp = current->next;
					current->next = new;
					new->next = tmp;
					break;
				}
				current = current->next;
			}
		}

	return (new);
}
