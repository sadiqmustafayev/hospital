from modeltranslation.translator import translator, TranslationOptions
from core.models import Blogs, Doctors


class BlogsTranslationOptions(TranslationOptions):
  fields = (
    'title',
    'description',
  )


translator.register(Blogs, BlogsTranslationOptions)

 
class DoctorsTranslationOptions(TranslationOptions):
  fields = ('educational_history', )


translator.register(Doctors, DoctorsTranslationOptions)
