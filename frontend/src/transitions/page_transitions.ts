export const page_transitions = {
  duration: 0.8,
  ease: [0.83, 0, 0.17, 1],
};

export const layout_motion = {
  initial: { opacity: 0 },
  animate: {
    opacity: 1,
    transition: {
      duration: page_transitions.duration,
      ease: page_transitions.ease,
    },
  },
  exit: {
    opacity: 0,
    transition: {
      duration: page_transitions.duration,
      ease: page_transitions.ease,
    },
  },
};
