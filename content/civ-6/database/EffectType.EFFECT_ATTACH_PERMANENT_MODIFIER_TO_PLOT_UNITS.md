---
tags:
- EffectType
title: EFFECT_ATTACH_PERMANENT_MODIFIER_TO_PLOT_UNITS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ATTACH_PERMANENT_MODIFIER_TO_PLOT_UNITS
>
> * Class: `Unknown`
> * Parameters:
>	* ModifierId `Unknown`

## Samples

```SQL {title="SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_ON_DEAD_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_ON_DEAD_UNIT",
		"MODIFIER_ALL_COMBAT_RESULTS_APPLY_MODIFIER_TO_UNITS_ON_TILE",
		"THIS_COMBAT_RESULTS_IN_UNIT_DEATH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_ON_DEAD_UNIT",
		"ModifierId",
		"SANGUINE_PACT_VAMPIRE_COMBAT_STRENGTH_ATTACHMENT"
	);
	
```

