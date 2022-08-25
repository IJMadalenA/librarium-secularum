# Imported from Django.

def test_factory_create_object(self, model, factory):

    before_create = model.objects.count()

    new_object = factory()
    self.assertTrue(model.objects.filter(id=new_object.id).exists())
    self.assertEqual(model.objects.count(), before_create + 1)
