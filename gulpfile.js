const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const shell = require('gulp-shell');

// 
gulp.task('sass', function() {
  return gulp
    .src('f5/static/sass/**/*.scss')
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(gulp.dest('f5/static/css'));
});

gulp.task('watch', function() {
  gulp.watch('f5/static/sass/**/*.scss', gulp.series('sass'));
});

gulp.task('collectstatic', shell.task('python manage.py collectstatic'));
gulp.task('reloadserver', shell.task('reloadserver'));
gulp.task('default', gulp.series('sass', 'watch'));
