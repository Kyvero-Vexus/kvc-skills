(in-package :common-lisp-user)

(defpackage :gadget-form-app
  (:use :clim :clim-lisp)
  (:export #:run-gadget-form-app))

(in-package :gadget-form-app)

(defun copy-input-into-output (gadget value)
  (declare (ignore gadget))
  (with-application-frame (frame)
    (let ((target (find-pane-named frame 'mirror-output)))
      (when target
        (setf (gadget-value target) value)))))

(defun commit-input (gadget)
  (with-application-frame (frame)
    (let ((target (find-pane-named frame 'committed-output)))
      (when target
        (setf (gadget-value target)
              (gadget-value gadget))))))

(define-application-frame gadget-form ()
  ()
  (:panes
   (input :text-field
          :value-changed-callback #'copy-input-into-output
          :activate-callback #'commit-input)
   (mirror-output :text-field :editable-p nil)
   (committed-output :text-field :editable-p nil))
  (:layouts
   (default (vertically () input mirror-output committed-output))))

(defun run-gadget-form-app ()
  (run-frame-top-level
   (make-application-frame 'gadget-form)))
