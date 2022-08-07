---
tags:
- EffectType
title: EFFECT_ADJUST_PROJECT_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PROJECT_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* ProjectType `String`
>		* [Projects.ProjectType]

## Samples

```SQL {title="EDUCATOR_FASTER_MANHATTAN_PROJECT_RESEARCH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"EDUCATOR_FASTER_MANHATTAN_PROJECT_RESEARCH",
		"MODIFIER_SINGLE_CITY_ADJUST_PROJECT_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EDUCATOR_FASTER_MANHATTAN_PROJECT_RESEARCH",
		"Amount",
		30
	),
	(
		"EDUCATOR_FASTER_MANHATTAN_PROJECT_RESEARCH",
		"ProjectType",
		"PROJECT_MANHATTAN_PROJECT"
	);
	
```

