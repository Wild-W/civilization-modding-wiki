---
tags:
- EffectType
title: EFFECT_ADJUST_ADDITIONAL_PILLAGING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ADDITIONAL_PILLAGING
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]
>	* PlunderType `String`
>		* PLUNDER_CULTURE>		  PLUNDER_FAITH>		  PLUNDER_GOLD>		  PLUNDER_HEAL>		  PLUNDER_SCIENCE

## Samples

```SQL {title="TRAIT_LEADER_PILLAGE_SCIENCE_MINES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_LEADER_PILLAGE_SCIENCE_MINES",
		"MODIFIER_PLAYER_ADJUST_ADDITIONAL_PILLAGING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_LEADER_PILLAGE_SCIENCE_MINES",
		"Amount",
		15
	),
	(
		"TRAIT_LEADER_PILLAGE_SCIENCE_MINES",
		"ImprovementType",
		"IMPROVEMENT_MINE"
	),
	(
		"TRAIT_LEADER_PILLAGE_SCIENCE_MINES",
		"PlunderType",
		"PLUNDER_SCIENCE"
	);
	
```

