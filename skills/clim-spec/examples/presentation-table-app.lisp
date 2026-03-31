(in-package :common-lisp-user)

(defpackage :presentation-table-app
  (:use :clim :clim-lisp)
  (:export #:run-presentation-table-app))

(in-package :presentation-table-app)

(defclass task ()
  ((title :initarg :title :reader task-title)
   (status :initarg :status :reader task-status)))

(define-presentation-type task ())

(defvar *tasks*
  (list (make-instance 'task :title "Write frame" :status :todo)
        (make-instance 'task :title "Add presentations" :status :doing)
        (make-instance 'task :title "Wire commands" :status :done)))

(define-application-frame task-browser ()
  ()
  (:pointer-documentation t)
  (:panes
   (table :application :display-function #'display-task-table)
   (interactor :interactor :height 200))
  (:layouts
   (default (vertically () table interactor))))

(defun display-task-table (frame pane)
  (declare (ignore frame))
  (formatting-table (pane :x-spacing '(2 :character))
    (formatting-row (pane)
      (formatting-cell (pane) (write-string "Task" pane))
      (formatting-cell (pane) (write-string "Status" pane)))
    (dolist (task *tasks*)
      (formatting-row (pane)
        (formatting-cell (pane)
          (with-output-as-presentation (pane task 'task)
            (write-string (task-title task) pane)))
        (formatting-cell (pane)
          (format pane "~A" (task-status task)))))))

(define-task-browser-command (com-describe-task :name t)
    ((task 'task :gesture :select))
  (format t "Task ~A is ~A.~%" (task-title task) (task-status task)))

(defun run-presentation-table-app ()
  (run-frame-top-level
   (make-application-frame 'task-browser)))
