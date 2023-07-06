const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const shell = require('gulp-shell');

// Watches for changes in /static/sass
gulp.task('watch', function() {
  gulp.watch('f5/static/sass/**/*.scss', gulp.series('sass', 'collectstatic', 'restartserver'));
});

// Compiles Sass from /static/sass to /static/css
gulp.task('sass', function() {
  return gulp
    .src('f5/static/sass/**/*.scss')
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(gulp.dest('f5/static/css'));
});

// Compiles Sass and watches for changes
gulp.task('default', gulp.series('sass', 'watch'));

// Runs collectstatic to update static files; 
// Note: always overwrites due to --noinput
gulp.task('collectstatic', shell.task('python manage.py collectstatic --noinput'));

// Restarts Gunicorn service
gulp.task('restartgunicorn', shell.task('sudo systemctl restart gunicorn.service'));

// Restarts Nginx service
gulp.task('restartnginx', shell.task('sudo systemctl restart nginx.service'));

// Task to restart Gunicorn and Nginx services
gulp.task('restartserver', gulp.series('restartgunicorn', 'restartnginx'));