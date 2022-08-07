---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_UNIT_PRODUCTION_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_UNIT_PRODUCTION_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="KILWA_SINGLE_ADDPRODUCTIONUNITS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"KILWA_SINGLE_ADDPRODUCTIONUNITS",
		"MODIFIER_SINGLE_CITY_ADJUST_UNIT_PRODUCTION_MODIFIER",
		"MILITARISTIC_SUZERAIN_1_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"KILWA_SINGLE_ADDPRODUCTIONUNITS",
		"Amount",
		15
	);
	
```

