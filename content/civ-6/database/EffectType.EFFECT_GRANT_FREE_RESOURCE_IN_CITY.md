---
tags:
- EffectType
title: EFFECT_GRANT_FREE_RESOURCE_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FREE_RESOURCE_IN_CITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples
```SQL {title="GREATPERSON_GRANT_JEANS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GRANT_JEANS",
		"MODIFIER_SINGLE_CITY_GRANT_RESOURCE_IN_CITY",
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
		"GREATPERSON_GRANT_JEANS",
		"Amount",
		2
	),
	(
		"GREATPERSON_GRANT_JEANS",
		"ResourceType",
		"RESOURCE_JEANS"
	);
	
```

