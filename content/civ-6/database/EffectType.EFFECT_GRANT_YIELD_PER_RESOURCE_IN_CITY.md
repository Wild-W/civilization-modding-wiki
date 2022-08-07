---
tags:
- EffectType
title: EFFECT_GRANT_YIELD_PER_RESOURCE_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_YIELD_PER_RESOURCE_IN_CITY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* Improved `Unknown`
>	* ResourceType `Unknown`
>	* YieldType `Unknown`

## Samples
```SQL {title="PROJECT_COMPLETION_MODIFIER_LEY_LINE_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"PROJECT_COMPLETION_MODIFIER_LEY_LINE_SCIENCE",
		"MODIFIER_GRANT_YIELD_PER_RESOURCE_TYPE_IN_CITY",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_MODIFIER_LEY_LINE_SCIENCE",
		"Amount",
		500
	),
	(
		"PROJECT_COMPLETION_MODIFIER_LEY_LINE_SCIENCE",
		"Improved",
		0
	),
	(
		"PROJECT_COMPLETION_MODIFIER_LEY_LINE_SCIENCE",
		"ResourceType",
		"RESOURCE_LEY_LINE"
	),
	(
		"PROJECT_COMPLETION_MODIFIER_LEY_LINE_SCIENCE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

