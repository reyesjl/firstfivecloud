// Description: Gulp tasks for compiling sass and running django server
const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const shell = require('gulp-shell');

// watches for changes in /static/sass
gulp.task('watch', function() {
  gulp.watch('f5/static/sass/**/*.scss', gulp.series('sass', 'collectstatic', 'reloadserver'));
});

// compiles sass from /static/sass to /static/css
gulp.task('sass', function() {
  return gulp
    .src('f5/static/sass/**/*.scss')
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(gulp.dest('f5/static/css'));
});

// compiles sass and watches for changes
gulp.task('default', gulp.series('sass', 'watch'));

// runs django server using shell alias
gulp.task('reloadserver', shell.task('reloadserver'));

// runs collectstatic to update static files; 
// note: always overwrites due to --noinput
gulp.task('collectstatic', shell.task('python manage.py collectstatic --noinput'));
