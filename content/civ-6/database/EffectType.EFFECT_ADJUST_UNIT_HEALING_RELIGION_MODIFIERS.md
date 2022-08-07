---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_HEALING_RELIGION_MODIFIERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_HEALING_RELIGION_MODIFIERS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* Type `String`

## Samples

```SQL {title="HOLY_WATERS_HEALING_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"HOLY_WATERS_HEALING_MODIFIER",
		"MODIFIER_ALL_UNITS_ADJUST_HEAL_RELIGION_PER_TURN",
		"HOLY_WATERS_HEALING_MODIFIER_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HOLY_WATERS_HEALING_MODIFIER",
		"Amount",
		10
	),
	(
		"HOLY_WATERS_HEALING_MODIFIER",
		"Type",
		"ALL"
	);
	
```

