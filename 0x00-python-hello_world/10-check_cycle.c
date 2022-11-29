#include "lists.h"

/**
 * check_cycle- Checks if a List has a loop
 * @list: pointer to list to be freed
 * description: Makes use of Floyd's Cycle Finding Algorithm
 * example: sourced from :
 * https://www.youtube.com/watch?v=Aup0kOWoMVg
 * Return: void
 */
int check_cycle(listint_t *list)
{
	listint_t *ftemp;
	listint_t *stemp;

	/* Set both pointers to point to head of list*/
	ftemp = list;
	stemp = list;

	while (ftemp != NULL && stemp != NULL && ftemp->next != NULL)
	{
		stemp = stemp->next;
		ftemp = ftemp->next->next;

		if (stemp == ftemp)
		{
			return (1);
		}
	}
	return (0);

}
