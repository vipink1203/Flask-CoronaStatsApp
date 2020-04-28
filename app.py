from dashboard import app,db,Corona
from flask import render_template,redirect,request,url_for,flash
from dashboard.coronastats import stat
from sqlalchemy.exc import IntegrityError


@app.route('/')
def index():

    data = Corona.query.all()
    return render_template('index.html',data=data)




@app.route('/refresh')
def refresh():
    info = stat()
    try:
        if Corona.query.filter_by(country='India').first():
            flash('Data already exist, please press delete and then refresh!')
            return redirect(url_for('index'))
        else:    
            for details in info:
                country = details['Country']
                deaths = details['Deaths']
                confirmed = details['Confirmed']
                recovered = details['Recovered']
                active = details['Active']
                updated = details['Last_updated']
                
                # Passing the data to model
                each_items = Corona(country,deaths,confirmed,recovered,active,updated)
                
                # Saving all data in database
                db.session.add(each_items)
                db.session.commit()
            flash('All Data Updated!')
            return redirect(url_for('index'))
    except IntegrityError:
        flash("Database Refreshed!", "error")
        return redirect(url_for('index'))


@app.route('/delete')
def delete():
    db.session.query(Corona).delete()
    db.session.commit()
    flash('All data deleted! Please refresh if you need new data')
    return redirect(url_for('index'))
    

if __name__ == "__main__":
    app.run(debug=True)
