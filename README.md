# ShipCompliant

The site can be found at http://afternoon-shelf-4487.herokuapp.com/

This site is built using Python built on the Django framework. For the small amount of time I had to build the site, I felt 
comfortable grabbing some prewritten code from another project (which can indirectly show my ability to write reuseable
code).

The site also utilizes Twitter Bootstrap 3.0.

A few things that I felt unhappy about:
<ul>
  <li>The layout of the home page. It could really use some styling work.</li>
  <li>
    The concept that saving a new ingredient does an entire page refresh
    <ul>
      <li>
        (It should be very simple to write the ajax call to simply add a new item to the DB and 
        then also add it the the drop down list of choice.
      </li>
    </ul>
  </li>
</ul>
