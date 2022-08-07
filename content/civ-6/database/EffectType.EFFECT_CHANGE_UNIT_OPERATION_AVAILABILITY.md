---
tags:
- EffectType
title: EFFECT_CHANGE_UNIT_OPERATION_AVAILABILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_CHANGE_UNIT_OPERATION_AVAILABILITY
>
> * Class: `UNITS`
> * Parameters:
>	* Available `Boolean`
>	* OperationType `String`

## Samples

```SQL {title="SOOTHSAYER_EMERGENCY_GRANT_OPERATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SOOTHSAYER_EMERGENCY_GRANT_OPERATION",
		"MODIFIER_ALL_UNITS_DISABLE_OPERATION",
		"EMERGENCY_IS_SOOTHSAYER_UNIT_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SOOTHSAYER_EMERGENCY_GRANT_OPERATION",
		"Available",
		1
	),
	(
		"SOOTHSAYER_EMERGENCY_GRANT_OPERATION",
		"OperationType",
		"UNITOPERATION_SOOTHSAYER_SACRIFICE"
	);
	
```

