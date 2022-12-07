// C program for array implementation of stack
#include "lists.h"
 
// function to create a stack of given capacity. It initializes size of
// stack as 0
struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

void expand_stack(struct Stack *stack)
{
	/**
	 * stack should only expand as per the required size
	 * needed to hold current push item
	 * only handles integers therefore use sizeof(int)
	 */
	// there is no need to cast to an int unless it's c++
	stack->array = realloc(stack->array, sizeof(int) * 10);
	/* update capacity*/
	stack->capacity++;
}
 
// Stack is full when top is equal to the last index
int isFull(struct Stack* stack)
{
    return stack->top == stack->capacity - 1;
}
 
// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack)
{
    return stack->top == -1;
}
 
// Function to add an item to stack.  It increases top by 1
void push(struct Stack* stack, int item)
{
    if (isFull(stack))
    {
	    /*if stack is full dynamically expand its size by 1.5 using realloc*/
	    printf("\narray capacity expanded from %d ",stack->capacity);
	    expand_stack(stack);
        printf("to %d capacity\n",stack->capacity);
	    push(stack, item);
        //return;
    }
    else {
        stack->array[++stack->top] = item;
        printf("%d pushed to stack\n", item);
    }
}
 
// Function to remove an item from stack.  It decreases top by 1
int pop(struct Stack* stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top--];
}
 
// Function to return the top from stack without removing it
int peek(struct Stack* stack)
{
    if (isEmpty(stack))
        return INT_MIN;
    return stack->array[stack->top];
}

// Function that returns boolean value
int is_palindrome(listint_t **head)
{

        // Temp pointer
        listint_t *slow = *head;
        listint_t *walker = *head;

        // Create a stack
	struct Stack* stack = createStack(0);


        // First traversal to push all the elements to stack
        while(slow != NULL){
                push(stack,slow->n);
                slow = slow->next;
        }

        // Second Traversal to compare the stack and node
        while(walker != NULL ){
		//printf("val %d == %d\n", walker->n, peek(stack));

            int i= peek(stack);
            pop(stack);

            // Compare data
            if(walker->n != i){
                return 0;
            }
        walker=walker->next;
        }

return 1;
}
