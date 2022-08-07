---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_BUILD_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_BUILD_CHARGES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* UnitType `Unknown`

## Samples

```SQL {title="PYRAMID_ADJUST_BUILDER_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"PYRAMID_ADJUST_BUILDER_CHARGES",
		"MODIFIER_PLAYER_UNITS_ADJUST_BUILDER_CHARGES",
		"UNIT_IS_BUILDER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PYRAMID_ADJUST_BUILDER_CHARGES",
		"Amount",
		1
	);
	
```


```SQL {title="SECRET_SOCIETY_GRANT_TWO_VAMPIRE_BUILDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SECRET_SOCIETY_GRANT_TWO_VAMPIRE_BUILDS",
		"MODIFIER_PLAYER_UNITS_ADJUST_BUILDER_CHARGES",
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
		"SECRET_SOCIETY_GRANT_TWO_VAMPIRE_BUILDS",
		"Amount",
		2
	),
	(
		"SECRET_SOCIETY_GRANT_TWO_VAMPIRE_BUILDS",
		"UnitType",
		"UNIT_VAMPIRE"
	);
	
```

