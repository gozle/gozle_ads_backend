from celery import shared_task


@shared_task
def hide_the_model(model, pk: int):
    queryset = model.objects.get(id=pk)
    queryset.set_as_hidden()
