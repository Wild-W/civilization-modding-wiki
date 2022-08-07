---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PROPERTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PROPERTY
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Unknown`
>	* Key `Unknown`

## Samples

```SQL {title="SECRET_SOCIETIES_ENABLE_VAMPIRE_PILLAGE_HEALING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SECRET_SOCIETIES_ENABLE_VAMPIRE_PILLAGE_HEALING",
		"MODIFIER_ALL_UNITS_ADJUST_PROPERTY",
		"THIS_UNIT_IS_A_VAMPIRE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SECRET_SOCIETIES_ENABLE_VAMPIRE_PILLAGE_HEALING",
		"Amount",
		50
	),
	(
		"SECRET_SOCIETIES_ENABLE_VAMPIRE_PILLAGE_HEALING",
		"Key",
		"HEAL_ON_PILLAGE"
	);
	
```

