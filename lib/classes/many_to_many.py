from collections import Counter
class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        #appends all articles to the "all" list so they can be accessible
        
    @property
    def title(self):
        return self._title
        # ._ means private to the class and should not be accesssed or modified directly from outside the class
        
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "title"):
            self._title = title
        #checks if value being passed in (title) is a string and len b/t 5-50 characters
        #checks if attribute "title" does not already exist for the object
        #if conditions are met, sets the value to the ._title attribute
        #if the obj does not already have a title attribute, & new 'title' meets the conditions, assign new title to ._title attrb
            
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        #checks if value being passed in (author) is instance of Author class
        #if condition is true then sets ._author attribute to the value
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        #checks if value being passed in (magazine) is instance of Magazine class
        #if condition is true then sets ._magazine attribute to the value
class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        #checks if value passed to the setter is a string 
        #checks if instance of self does not already have an attribute of "name"
        #this restricts it from being changed b/c once it is set during instn, "not hasattr(self,"name")" will no longer
        #be true and attempts to change it will be blocked
        
    def articles(self):
        return [article for article in Article.all if article.author == self]
        #iterates over articles in Article.all 
        #checks if article's author attribute matches 'self'
        #if condition is true returns list containing all articles by current author
        
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
        #calls articles() method from above ^ to get all articles by current author
        #for each article, retrieves the magazine associated w/ it ('article.magazine')
        #converts list to set to ensure each entry is "unique" (appears once)
        #converts back to a list and returns it

    def add_article(self, magazine, title):
        new_article = Article(author=self, magazine=magazine, title=title)
        return new_article
        #requires parameters of magazine & title
        #creates an instance of Article class w/ attributes:
        #author - the current instance of self
        #magazine - the magazine instance passed as an arguement
        #title - the title passed as an arguement
        #returns newly created instance of Article

    def topic_areas(self):
        categories = {article.magazine.category for article in self.articles()}
        return list(categories) if categories else None
        #uses set comprehension to create a set
        #iterates over each article in list that self.articles() returns & retrieves catgry
        #if categories isnt empty it turns set into a list, otherwise returns None
        #use article.magazine.category because category is not an attribute of Article, but an attribute of
        #the "Magazine" object associated w/ each article 

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name,str) and 2 <= len(name) <= 16:
            self._name = name
        #checks if name is type of string and b/t 2-16 characters
        #allows the 'name' attribute to be changed after instn w/o restrictions
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        #checks if value passed in(category) is a string and the length of cat is >0
        #if conditions are met, sets ._category attribute to value(category)

    def articles(self):
        return[article for article in Article.all if article.magazine == self]
        #iterate over articles
        #create list if magazine is same instance as self

    def contributors(self):
        return list(set([article.author for article in self.articles()]))
        #calls articles() method from above to retrieve list of articles
        #iterates over articles and creates a set of authors so that list is unique
        #converts set to list

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
        #iterate over all articles & create list of titles
        #if titles is not empty, return titles otherwise return None

    def contributing_authors(self):
        author_count = Counter(article.author for article in self.articles())
        return [author for author, count in author_count.items() if count >2] or None
        #iterate over articles and find authors
        #pass authors to Counter constructor, which creates a dict-like object where author is the
        #key and the value is the count of author in the magazine
        #then iterate over each pair and filter based on count being > 2
        #returns list of auth who have more than 2 articles for the magazine, or return None if none are found
        