---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_HEALING_MODIFIERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_HEALING_MODIFIERS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* Type `String`

## Samples

```SQL {title="GOD_OF_HEALING_UNIT_HEALING_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"GOD_OF_HEALING_UNIT_HEALING_MODIFIER",
		"MODIFIER_PLAYER_UNITS_ADJUST_HEAL_PER_TURN",
		"PLOT_ADJACENT_INCLUDE_HOLY_SITE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOD_OF_HEALING_UNIT_HEALING_MODIFIER",
		"Amount",
		30
	),
	(
		"GOD_OF_HEALING_UNIT_HEALING_MODIFIER",
		"Type",
		"ALL"
	);
	
```

