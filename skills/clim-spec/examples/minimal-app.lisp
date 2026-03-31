(in-package :common-lisp-user)

(defpackage :minimal-mcclim-app
  (:use :clim :clim-lisp)
  (:export #:run-minimal-mcclim-app))

(in-package :minimal-mcclim-app)

;; Minimal CLIM/McCLIM application skeleton:
;; - one application frame
;; - one interactor pane
;; - default layout
;; - runner function

(define-application-frame minimal-app ()
  ()
  (:panes
   (main :interactor :height 400 :width 700))
  (:layouts
   (default main)))

(defun run-minimal-mcclim-app ()
  (run-frame-top-level
   (make-application-frame 'minimal-app)))
